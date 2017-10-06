// CaptureScreen.cpp : 定义控制台应用程序的入口点。
//

#include "start.h"
#include<windows.h>

#define PALVERSION 0x300
#define CAP_SHOW_MODE_STRTCH 1
#define CAP_SHOW_MODE_NOSTRTCH 0

HBITMAP ghBitmap = NULL;
RECT rectShow;
LPSTR szCaptureWindowName = NULL;
//DWORD WINAPI
int WinMain(HINSTANCE, HINSTANCE, LPSTR, int);
LRESULT CALLBACK MainWndProc(HWND, UINT, WPARAM, LPARAM);
HBITMAP ScreenCapture(LPSTR filename, WORD BitCount, LPRECT);
VOID DoPaint(HWND hWnd);


int WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nCmdShow
)
{
	// 调用API函数 MessageBox
	/*MessageBox(NULL,
	TEXT("开始学习Windows编程"),
	TEXT("消息对话框"),
	MB_OK);

	return 0;*/
	WNDCLASSEX wcx;
	HWND hwnd;
	MSG msg;
	WORD wport = 80;
	BOOL fGotMessage;
	HWND hwndCap = NULL;

	if (szCaptureWindowName != NULL)
	{
		hwndCap = FindWindow(NULL, szCaptureWindowName);
		if (!GetWindowRect(hwndCap, &rectShow))
		{
			MessageBox(NULL, "can not find window to capture", "error", MB_OK);
			return 0;
		}
	}
	wcx.cbSize = sizeof(wcx);
	wcx.style = CS_HREDRAW | CS_VREDRAW;
	wcx.lpfnWndProc = 0;
	wcx.cbClsExtra = 0;
	wcx.hInstance = hInstance;
	wcx.hIcon = LoadIcon(NULL, MAKEINTRESOURCE(IDI_APPLICATION));
	wcx.hCursor = LoadCursor(NULL, IDC_ARROW);
	wcx.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
	wcx.lpszMenuName = NULL;
	wcx.lpszClassName = "MainWClass";
	wcx.hIconSm = NULL;
	if (!RegisterClassEx(&wcx))
	{
		return 1;
	}
	//创建窗口
	hwnd = CreateWindow("MainWClass", "CAP", WS_OVERLAPPEDWINDOW | WS_CLIPCHILDREN | WS_CLIPSIBLINGS | WS_MAXIMIZE | WS_POPUPWINDOW,
		CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, (HWND)NULL, (HMENU)NULL, hInstance, (LPVOID)NULL);
	if (!hwnd)
	{
		return 1;
	}
	//截取屏幕
	ghBitmap = ScreenCapture("F:\\aaa.bmp", 32, &rectShow);
	ShowWindow(hwnd, nCmdShow);
	UpdateWindow(hwnd);
	while ((fGotMessage = GetMessage(&msg, (HWND)NULL, 0, 0)) != 0 && fGotMessage != -1)
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return msg.wParam;
	UNREFERENCED_PARAMETER(lpCmdLine);

}

HBITMAP ScreenCapture(LPSTR filename, WORD BitCount, LPRECT lpRect)
{
	HBITMAP hBitmap;
	//显示器屏幕DC
	HDC hScreenDC = CreateDC("display", NULL, NULL, NULL);
	HDC hmenDC = CreateCompatibleDC(hScreenDC);
	//显示器屏幕的宽和高
	int ScreenWidth = GetDeviceCaps(hScreenDC, HORZRES);
	int ScreenHeight = GetDeviceCaps(hScreenDC, VERTRES);

	HBITMAP hOldBM;
	//保存位图数据
	PVOID lpvpxldata;
	//截取获取的长度及起点
	INT ixStart;
	INT iyStart;
	INT iX;
	INT iY;
	//位图数据大小
	DWORD dwBitmapArraySize;

	DWORD nBitsOffset;
	DWORD lImageSize;
	DWORD lFileSize;

	BITMAPINFO bmInfo;

	BITMAPFILEHEADER bmFileHeader;
	HANDLE hbmfile;
	DWORD dwWritten;

	if (lpRect == NULL)
	{
		ixStart = iyStart = 0;
		iX = ScreenWidth;
		iY = ScreenHeight;
	}
	else
	{
		ixStart = lpRect->left;
		iyStart = lpRect->top;
		iX = lpRect->right - lpRect->left;
		iY = lpRect->bottom - lpRect->top;
	}
	hBitmap = CreateCompatibleBitmap(hScreenDC, iX, iY);
	hOldBM = (HBITMAP)SelectObject(hmenDC, hBitmap);
	BitBlt(hmenDC, 0, 0, iX, iY, hScreenDC, ixStart, iyStart, SRCCOPY);
	hBitmap = (HBITMAP)SelectObject(hmenDC, hOldBM);
	if (filename == NULL)
	{
		DeleteDC(hScreenDC);
		DeleteDC(hmenDC);
		return hBitmap;
	}

	dwBitmapArraySize = ((((iX * 32) + 31)&~31) >> 3)*iY;
	lpvpxldata = HeapAlloc(GetProcessHeap(), HEAP_NO_SERIALIZE, dwBitmapArraySize);
	ZeroMemory(lpvpxldata, dwBitmapArraySize);

	ZeroMemory(&bmInfo, sizeof(BITMAPINFO));
	bmInfo.bmiHeader.biSize = sizeof(PBITMAPINFOHEADER);
	bmInfo.bmiHeader.biWidth = iX;
	bmInfo.bmiHeader.biHeight = iY;
	bmInfo.bmiHeader.biPlanes = 1;
	bmInfo.bmiHeader.biBitCount = BitCount;
	bmInfo.bmiHeader.biClrImportant = BI_RGB;

	ZeroMemory(&bmFileHeader, sizeof(BITMAPFILEHEADER));
	nBitsOffset = sizeof(BITMAPFILEHEADER) + bmInfo.bmiHeader.biSize;
	lImageSize = ((((bmInfo.bmiHeader.biWidth*bmInfo.bmiHeader.biBitCount) + 31)& ~31) >> 3)*bmInfo.bmiHeader.biHeight;
	lFileSize = nBitsOffset + lImageSize;
	bmFileHeader.bfOffBits = nBitsOffset;

	GetDIBits(hmenDC, hBitmap, 0, bmInfo.bmiHeader.biHeight, lpvpxldata, &bmInfo, DIB_RGB_COLORS);
	hbmfile = CreateFile(filename, GENERIC_WRITE, FILE_SHARE_WRITE, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);

	if (hbmfile == INVALID_HANDLE_VALUE)
	{
		MessageBox(NULL, "create file error", "error", MB_OK);
	}
	WriteFile(hbmfile, &bmFileHeader, sizeof(BITMAPCOREHEADER), &dwWritten, NULL);
	WriteFile(hbmfile, &bmInfo, sizeof(BITMAPINFO), &dwWritten, NULL);
	WriteFile(hbmfile, lpvpxldata, lImageSize, &dwWritten, NULL);
	CloseHandle(hbmfile);


	HeapFree(GetProcessHeap(), HEAP_NO_SERIALIZE, lpvpxldata);
	ReleaseDC(0, hScreenDC);
	DeleteDC(hmenDC);
	return hBitmap;
}

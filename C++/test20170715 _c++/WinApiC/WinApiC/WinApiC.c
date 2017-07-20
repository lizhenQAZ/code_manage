#include "windows.h"

#pragma comment (lib, "User32.lib")

int APIENTRY WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR  lpComdLine,
	int nCmdShow
)
{
	MessageBox(NULL, TEXT("HAHA"), TEXT("NiHao"), MB_OK);
	return 0;
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CaptureScreenCS
{
    public partial class Form1 : Form
    {
        bool mouseDown = false, havePainted = false;
        Point start, end;
        Point start1, end1;
        Size size = new Size(0, 0);
        bool saveFile = true;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ReadyToCaptrue();
            saveFile = true;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            start = e.Location;
            mouseDown = true;
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (size.Width != 0 && size.Height != 0)
            {
                ControlPaint.DrawReversibleFrame(new Rectangle(start1, size), Color.Transparent, FrameStyle.Dashed);
                havePainted = false;
            }
            end = e.Location;
            if (start.X > end.X)
            {
                int temp = end.X;
                end.X = start.X;
                start.X = temp;
            }

            if (start.Y > end.Y)
            {
                int temp = end.Y;
                end.Y = start.Y;
                start.Y = temp;
            }
            this.Opacity = 0.0;
            Thread.Sleep(200);
            if (end.X - start.X > 0 && end.Y - start.Y > 0)
            {
                Bitmap bit = new Bitmap(end.X - start.X, end.Y - start.Y);
                Graphics g = Graphics.FromImage(bit);
                g.CopyFromScreen(start, new Point(0, 0), bit.Size);
                if (saveFile)
                {
                    SaveFileDialog saveFileDialog = new SaveFileDialog();
                    saveFileDialog.Filter = "png|*.png|bmp|*.bmp|jpg|*.jpg|gif|*.gif";
                    if (saveFileDialog.ShowDialog() != DialogResult.Cancel)
                    {
                        bit.Save(saveFileDialog.FileName);
                    }
                }
                else
                {
                    Clipboard.SetImage(bit);
                }
                g.Dispose();
            }
            this.WindowState = FormWindowState.Normal;
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            panel1.Visible = true;
            this.Opacity = 1;
            mouseDown = false;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (mouseDown)
            {
                if (size.Width != 0 && size.Height != 0 && havePainted)
                {
                    ControlPaint.DrawReversibleFrame(new Rectangle(start1, size), Color.Transparent, FrameStyle.Dashed);
                }
                end1 = e.Location;
                size.Width = Math.Abs(end1.X - start.X);
                size.Height = Math.Abs(end1.Y - start.Y);
                start1.X = (start.X > end1.X) ? end1.X : start.X;
                start1.Y = (start.Y > end1.Y) ? end1.Y : start.Y;

                if (size.Width != 0 && size.Height != 0)
                {
                    ControlPaint.DrawReversibleFrame(new Rectangle(start1, size), Color.Transparent, FrameStyle.Dashed);
                    havePainted = true;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ReadyToCaptrue();
            saveFile = false;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void ReadyToCaptrue()
        {
            this.Opacity = 0.1;
            panel1.Visible = false;
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
        }
    }
}

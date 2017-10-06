using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsAppCapSrc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void 文件ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {

        }

        private void toolStripLabel1_Click(object sender, EventArgs e)
        {

        }

        private void toolStripProgressBar1_Click(object sender, EventArgs e)
        {

        }

        private void toolStripComboBox1_Click(object sender, EventArgs e)
        {

        }

        private void toolStripDropDownButton1_Click(object sender, EventArgs e)
        {

        }

        private void toolStripLabel5_Click(object sender, EventArgs e)
        {

        }

        private void toolStripLabel3_Click(object sender, EventArgs e)
        {

        }

        private void 荧光笔ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void 新建截图NToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void 另存为SToolStripMenuItem_Click(object sender, EventArgs e)
        {
            toolStripLabel2_Click(sender, e);
        }

        private void 发送到TToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("这一功能尚未实现！");
        }

        private void 退出XToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Exit?", "info", MessageBoxButtons.OKCancel) == DialogResult.OK)
                this.Close();
        }

        private void 复制CToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void 笔PToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("请到工具栏进行操作！");
        }

        private void 橡皮擦EToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void 选项OToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("此功能尚未实现！");
        }

        private void 帮助HToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("此功能尚未实现！");
        }

        private void 关于AToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            SaveFileDialog sfd = new SaveFileDialog();
            sfd.AddExtension = true;
            sfd.DefaultExt = "png";
            sfd.Filter = "*.png|*.bmp";
            sfd.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            if(sfd.ShowDialog() == DialogResult.OK)
            {
                string filename = sfd.FileName;
# Image image = this.pictur

            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}

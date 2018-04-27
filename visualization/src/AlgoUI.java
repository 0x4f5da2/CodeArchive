import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JSlider;
import javax.swing.JButton;
import javax.swing.JSeparator;
import javax.swing.SwingConstants;
import java.awt.EventQueue;
import java.awt.Font;
import javax.swing.JSpinner;
import javax.swing.SpinnerNumberModel;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class AlgoUI extends JFrame {

    private JPanel contentPane;
    private BoardPanel mainPanel;
    private JLabel valSize;
    private JSpinner spinnerX;
    private JSpinner spinnerY;
    private JSlider sizeSlider;
    private int uiStep;
    private int pow2[] = {1,2,4,8,16,32,64};


    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    AlgoUI frame = new AlgoUI();
                    frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }



    /**
     * Create the frame.
     */
    public AlgoUI() {
        uiStep = 0;
        setResizable(false);
        //setTitle(" \u7531\u9648\u81F3\u6210\u5236\u4F5C\u7684\u7B80\u964B\u7684\u68CB\u76D8\u8986\u76D6\u7B97\u6CD5\u53EF\u89C6\u5316\u8F6F\u4EF6");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 550, 650);
        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(contentPane);
        contentPane.setLayout(null);

        mainPanel = new BoardPanel();
        mainPanel.setBounds(20, 80, 512, 512);
//        mainPanel.getGraphics().fillRect(0,0,512,512);
        contentPane.add(mainPanel);

        //JLabel lblTitle = new JLabel("\u7B80\u964B\u7684\u68CB\u76D8\u8986\u76D6\u7B97\u6CD5\u53EF\u89C6\u5316\u8F6F\u4EF6");
        //lblTitle.setFont(new Font("等线", Font.PLAIN, 32));
        //lblTitle.setBounds(10, 28, 512, 42);
        //contentPane.add(lblTitle);

        sizeSlider = new JSlider();
        sizeSlider.setValue(1);
        sizeSlider.setMaximum(6);
        sizeSlider.setMinimum(1);
        sizeSlider.setBounds(551, 141, 235, 50);
        sizeSlider.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                valSize.setText(Integer.toString(pow2[sizeSlider.getValue()]));
                spinnerX.setModel(new SpinnerNumberModel(0,0,pow2[sizeSlider.getValue()]-1,1));
                spinnerY.setModel(new SpinnerNumberModel(0,0,pow2[sizeSlider.getValue()]-1,1));
                uiStep = 0;
                mainPanel.setUp((int)spinnerX.getValue(), (int)spinnerY.getValue(), pow2[sizeSlider.getValue()], uiStep);
                mainPanel.printComponent(mainPanel.getGraphics());
            }
        });
        contentPane.add(sizeSlider);

        JLabel lblSize = new JLabel("\u8BBE\u7F6E\u68CB\u76D8\u7684\u5927\u5C0F");
        lblSize.setFont(new Font("等线", Font.PLAIN, 16));
        lblSize.setBounds(551, 89, 283, 42);
        contentPane.add(lblSize);

        valSize = new JLabel("2");
        valSize.setFont(new Font("等线", Font.PLAIN, 24));
        valSize.setBounds(821, 141, 34, 50);
        contentPane.add(valSize);

        JLabel lblX = new JLabel("\u8BBE\u7F6E\u7279\u6B8A\u65B9\u683C\u7684\u6A2A\u5750\u6807\r\n");
        lblX.setFont(new Font("等线", Font.PLAIN, 16));
        lblX.setBounds(551, 201, 283, 42);
        contentPane.add(lblX);

        JButton nextStep = new JButton("\u4E0B\u4E00\u6B65");
        nextStep.setBounds(551, 425, 128, 80);
        nextStep.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                    uiStep++;
                    mainPanel.setUp((int) spinnerX.getValue(), (int) spinnerY.getValue(), pow2[sizeSlider.getValue()], uiStep);
                    mainPanel.printComponent(mainPanel.getGraphics());

            }
        });
        contentPane.add(nextStep);

        JSeparator separator = new JSeparator();
        separator.setOrientation(SwingConstants.VERTICAL);
        separator.setBounds(540, 80, 10, 512);
        contentPane.add(separator);

        spinnerX = new JSpinner();
        spinnerX.setModel(new SpinnerNumberModel(0, 0, 1, 1));
        spinnerX.setFont(new Font("等线", Font.PLAIN, 24));
        spinnerX.setBounds(661, 253, 173, 42);
        contentPane.add(spinnerX);

        JLabel lblY = new JLabel("\u8BBE\u7F6E\u7279\u6B8A\u65B9\u683C\u7684\u7EB5\u5750\u6807\r\n");
        lblY.setFont(new Font("等线", Font.PLAIN, 16));
        lblY.setBounds(551, 305, 283, 42);
        contentPane.add(lblY);

        spinnerY = new JSpinner();
        spinnerY.setModel(new SpinnerNumberModel(0, 0, 1, 1));
        spinnerY.setFont(new Font("等线", Font.PLAIN, 24));
        spinnerY.setBounds(661, 357, 173, 42);
        contentPane.add(spinnerY);

        JButton prevStep = new JButton("\u4E0A\u4E00\u6B65");
        prevStep.setBounds(706, 425, 128, 80);
        prevStep.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(uiStep > -1){
                    uiStep--;
                    mainPanel.setUp((int)spinnerX.getValue(), (int)spinnerY.getValue(), pow2[sizeSlider.getValue()], uiStep);
                    mainPanel.printComponent(mainPanel.getGraphics());
                }
            }
        });
        contentPane.add(prevStep);

        JButton showAns = new JButton("\u663E\u793A\u6700\u7EC8\u7ED3\u679C");
        showAns.setBounds(551, 515, 128, 80);
        showAns.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                uiStep = -1;
                mainPanel.setUp((int)spinnerX.getValue(), (int)spinnerY.getValue(), pow2[sizeSlider.getValue()], uiStep);
                mainPanel.printComponent(mainPanel.getGraphics());
            }
        });
        contentPane.add(showAns);

        JButton reset = new JButton("\u91CD\u7F6E");
        reset.setBounds(706, 515, 128, 80);
        reset.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                spinnerX.setModel(new SpinnerNumberModel(0,0,pow2[sizeSlider.getValue()]-1,1));
                spinnerY.setModel(new SpinnerNumberModel(0,0,pow2[sizeSlider.getValue()]-1,1));
                uiStep = 0;
                mainPanel.setUp((int)spinnerX.getValue(), (int)spinnerY.getValue(), pow2[sizeSlider.getValue()], uiStep);
                mainPanel.printComponent(mainPanel.getGraphics());
            }
        });
        contentPane.add(reset);

    }




    class BoardPanel extends JPanel{
        private int board[][];
        private int color[][];
        private int px,py;
        private int size;
        private int st;
        private int showStep;
        public Color colors[] = {Color.BLACK, new Color(242, 80, 34), new Color(127, 186, 0), new Color(0, 164, 239), new Color(255, 185, 0)};
        ArrayList<Point> visArr;



        public void setUp(int x, int y, int s, int ss) {
            this.board = new int[550][550];
            this.px = x;
            this.py = y;
            this.size = s;
            for(int i=0; i < size; i++){
                for(int j=0; j<size;j++){
                    board[i][j] = 0;
                }
            }
            this.st=1;
            this.showStep = ss;
        }

//        public static void main(String[] args){
//            BoardPanel boardPanel = new BoardPanel();
//            boardPanel.setUp(0,0,32);
//            boardPanel.run();
//        }

        private void recursive(int sx, int sy, int offset, int x, int y){
            if(offset==1){
                return;
            }
            int flag = 0;
            int thisStep = this.st++;
            offset/=2;
            if(x >= sx + offset){
                flag++;
            }
            if(y >= sy + offset){
                flag+=2;
            }
            if(flag==0){
                recursive(sx,sy,offset,x,y);
            } else {
                this.board[sx+offset-1][sy+offset-1] = thisStep;
                recursive(sx,sy,offset,sx+offset-1, sy+offset-1);
            }
            if(flag==1){
                recursive(sx+offset,sy,offset,x,y);
            } else {
                this.board[sx+offset][sy+offset-1] = thisStep;
                recursive(sx+offset,sy,offset,sx+offset, sy+offset-1);
            }
            if(flag==2){
                recursive(sx,sy+offset,offset,x,y);
            } else {
                this.board[sx+offset-1][sy+offset] = thisStep;
                recursive(sx,sy+offset,offset,sx+offset-1, sy+offset);
            }
            if(flag==3){
                recursive(sx+offset,sy+offset,offset,x,y);
            } else {
                this.board[sx+offset][sy+offset] = thisStep;
                recursive(sx+offset,sy+offset,offset,sx+offset, sy+offset);
            }

        }


        public void setColors(ArrayList<Point> points, int col){
            for(Point point:points){
                color[point.x][point.y] = col;
            }
        }

        public int getColors(ArrayList<Point> points){
            int used[] = {1,0,0,0,0};
            int dirx[] = {1,0,-1,0};
            int diry[] = {0,1,0,-1};
            for(Point point:points){
                for(int i=0;i<4;i++){
                    if(point.x + dirx[i] <0 || point.x + dirx[i] >= size ||point.y + diry[i] < 0 || point.y + diry[i]>=size){
                        continue;
                    }
                    if(color[point.x + dirx[i]][point.y + diry[i]] > 0){
                        used[color[point.x + dirx[i]][point.y + diry[i]]]=1;
                    }
                }
            }
            for(int i=0;i<5;i++){
                if(used[i]==0)
                    return i;
            }
            for(Point point:points){
                System.out.println(point);
            }
            System.out.println("--------------------");
            return 0;
        }


        public ArrayList<Point> dfs(int i, int j, int n){
            if(i<0||j<0||i>=size||j>=size){
                return null;
            }
            if(board[i][j] != n){
                return null;
            }

            if(visArr.indexOf(new Point(i,j))!=-1){
                return null;
            }
            visArr.add(new Point(i,j));
            ArrayList<Point> ret = new ArrayList<Point>();
            ret.add(new Point(i, j));
            ArrayList<Point> tmp = null;
            int dirx[] = {1,0,-1,0};
            int diry[] = {0,1,0,-1};
            for(int ii=0;ii<4;ii++) {
                if ((tmp = dfs(i + dirx[ii], j + diry[ii], n)) != null) {
                    ret.addAll(tmp);
                }
            }
            if(ret.size()>3){
                System.out.println("error");
            }
            return ret;
        }


        public void findColor(){
            color = new int[550][550];
            for(int i=0;i<size;i++){
                for(int j=0;j<size;j++){
                    color[i][j] = 0;
                }
            }

            for(int i=0;i<size;i++){
                for(int j=0;j<size;j++){
                    if(board[i][j] == 0 || color[i][j] > 0)
                        continue;
                    visArr = new ArrayList<Point>();
                    ArrayList<Point> aL = dfs(i,j,board[i][j]);
                    setColors(aL,getColors(aL));
                }
            }

        }

        public void run(){
            this.recursive(0,0, size,px, py);
            this.findColor();
            for(int i=0;i<size;i++){
                for(int j=0;j<size;j++){
                    System.out.format("%4s", Integer.toString(board[i][j]));
                }
                System.out.println("");
            }
            System.out.println("#####################################");
            for(int i=0;i<size;i++){
                for(int j=0;j<size;j++){
                    System.out.format("%4s", Integer.toString(color[i][j]));
                }
                System.out.println("");
            }
            System.out.println("#####################################");
            System.out.println("#####################################");

        }

        @Override
        protected void printComponent(Graphics g) {
            g.fillRect(0,0,this.getWidth(), this.getHeight());
            run();
            for(int i=0;i<this.size;i++){
                for(int j=0;j<this.size;j++){
                    if(showStep == -1 || board[i][j] <= showStep) {
                        g.setColor(colors[color[i][j]]);
                        g.fillRect(i*512/size,j*512/size,512/size,512/size);
                    }
                }
            }
        }
    }

}


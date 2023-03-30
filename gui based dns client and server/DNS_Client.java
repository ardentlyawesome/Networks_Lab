import java.io.*;
import java.net.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.lang.Exception;

class CreateDNSGUI extends JFrame implements ActionListener
{
    JButton b1;
    JPanel newPanel;
    JLabel userLabel, passLabel;
    String given_hostname;

    public static boolean has_finished = false;
    final JTextField textField1;
    CreateDNSGUI( ){    
        userLabel = new JLabel();
        userLabel.setText("Type a website:");  
        textField1 = new JTextField(30);   
        b1 = new JButton("SUBMIT"); 
        newPanel = new JPanel(new GridLayout(3, 1));
        newPanel.add(userLabel);   
        newPanel.add(textField1);  
        newPanel.add(b1);          
        add(newPanel, BorderLayout.CENTER);
        b1.addActionListener(this);  
        setTitle("DNS GUI");     
    }
    public void actionPerformed(ActionEvent ae)     
    {
        given_hostname = textField1.getText();
        has_finished = true;
    }
    public String getHostName()
    {
        return given_hostname;
    }
}

public class DNS_Client 
{
    static CreateDNSGUI form;
    public static void main(String args[]) throws Exception
    {
        String host; 
        int port; 
        
        //checking if the user chose an IP address and a port instead of the defaults (127.0.0.1, 8888)
        if (args.length == 2) 
        { 
           host = args[0]; 
           port = Integer.parseInt(args[1]); 
        } 
        else
        {
            System.out.println("-----------------------------------------");
            System.out.println("Usage: java DNS_Client <host name> <port>"); 
            System.out.println("Default host name: 127.0.0.1");
            System.out.println("Default port: 8888");
            System.out.println("-----------------------------------------\n");
            
            host = "127.0.0.1";
            port = 8888;
        }       
        
        System.out.println("Reaching DNS Server at " +host+ " with port " + port + "..."); 
        
        BufferedReader keyboard_input = new BufferedReader(new InputStreamReader(System.in));
        // System.out.print("Type a website: ");  
        // String given_hostname = keyboard_input.readLine();
        try
        {
            form = new CreateDNSGUI();
            form.setSize(300,100); 
            form.setVisible(true); 
        }
        catch(Exception e)
        {    
            JOptionPane.showMessageDialog(null, e.getMessage());
        }
        
        
        //setting up the socket and its timeout that we're going to use to access the server
        DatagramSocket client_socket = new DatagramSocket();
        client_socket.setSoTimeout(3000);
                
        InetAddress IP_address = InetAddress.getByName(host);
        byte[] send_data = new byte[1024];
        byte[] receive_data = new byte[1024];
        while (!form.has_finished)
        {
            System.out.print((form.has_finished) ? "Nice":"");

        }
        // System.out.println((form.has_finished) ? "Nice":"Stop it, get some help.");
        send_data = form.given_hostname.getBytes();
        
        //sending the given-by-user website to the server 
        DatagramPacket send_packet = new DatagramPacket(send_data, send_data.length, IP_address, port);
        client_socket.send(send_packet);
        
        //setting up the packet we will receive with the IP address of the given-by-user website 
        DatagramPacket receive_packet = new DatagramPacket(receive_data, receive_data.length);

        try
        {
            //receiving the IP address from the server and turning it to a string
            client_socket.receive(receive_packet);
            String server_response = new String(receive_packet.getData());
            
            String two_char_response = server_response.substring(0,2);
            
            //checking if the first two chars of the response are "-1", indicating that the address was not found
            if(two_char_response.equals("-1"))
                System.out.println("DNS server's response: NOT FOUND");
            else
                System.out.println("DNS server's response: " + server_response);
        } 
        catch (SocketTimeoutException e) 
        {
            System.out.println("Timeout reached. " + e);
        }
        
        client_socket.close();
    }
}


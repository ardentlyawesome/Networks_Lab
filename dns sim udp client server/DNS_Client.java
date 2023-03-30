import java.io.*;
import java.net.*;

public class DNS_Client
{
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
        
        BufferedReader keyboard_input = new BufferedReader(new InputStreamReader(System.in)); //create i/p stream
        System.out.print("Type a website: ");  
        String given_hostname = keyboard_input.readLine();
        
        //setting up the socket and its timeout that we're going to use to access the server
        DatagramSocket client_socket = new DatagramSocket();   //create client socket 
        client_socket.setSoTimeout(3000);
                
        InetAddress IP_address = InetAddress.getByName(host);  //translate hostname to IP address using DNS
        byte[] send_data = new byte[1024];
        byte[] receive_data = new byte[1024];
         
        send_data = given_hostname.getBytes();
        
        //sending the given-by-user website to the server 
        DatagramPacket send_packet = new DatagramPacket(send_data, send_data.length, IP_address, port); //create datagram packet(data to send, length, IPAddr, port)
        client_socket.send(send_packet);//send datagram to server
        
        //setting up the packet we will receive with the IP address of the given-by-user website 
        DatagramPacket receive_packet = new DatagramPacket(receive_data, receive_data.length); //read datagram from server

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


import java.net.*;
import java.io.*;

public class iterativeserver {
    //initialise socket and input stream

    private Socket socket= null;
    private ServerSocket server = null;
    private DataInputStream in = null;

    public iterativeserver(int port)
    {
        try
        {
            server = new ServerSocket(port);
            System.out.println("Server started");
            System.out.println("Waiting for a client..");
            socket = server.accept();
            System.out.println("Client Accepted");

            in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));

            String line = "";

            while (!line.equals("Over"))
            {
                try
                {
                    line = in.readUTF();
                    System.out.println(line);
                }
                catch(Exception i)
                {

                }
            }
            System.out.println("Closing connection");
            socket.close();

        }
        catch (Exception i)
        {

        }
    }

    public static void main(String args[]) throws BindException
    {
        int count = 0;
        iterativeserver server;
        while(true){
            try{
                server = new iterativeserver(5000);
                System.out.println("Client "+count+" Ended.");
                count++;
            }
            catch(Exception e){
                
            }
        }
    }
}

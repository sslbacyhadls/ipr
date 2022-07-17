import javax.servlet.ServletException;
import javax.servlet.http.*;
import java.io.IOException;


public class HelloServlet extends HttpServlet {
   protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
     String path = "/WEB-INF/view/index.html";
     req.getRequestDispatcher(path).forward(req, resp);
   }
}

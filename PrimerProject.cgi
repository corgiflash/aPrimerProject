#! /bin/bash
echo "Content-type:text/html"
echo ""

echo "<html>"
echo "<head>"
echo 'The URI of the request is '$REQUEST_URI
echo "<link rel = "stylesheet" type = "text/css" href = proj.css>"
echo "<title>COMP490 Project</title>"
echo "</head>"
echo "<body>"
echo "<div class = gif> <img src = "http://www.csun.edu/~dz382392/zeroGravityCat.gif"></div>"
/usr/bin/curl -s ${QUERY_STRING}
echo "</body></html>"
exit 0
def readFile(path: String) =
  scala.io.Source.fromFile(path).getLines.mkString("\n")

def createContents(s: String, div: String, js: String, out: String="") = {
  if (s.length==0) out else {
    if (s.split("\n").head == music)
  }
}

/* Test:
val fileContent = readFile("../template/sample_abc.txt")
val template = readFile("../template/template.txt")
 */


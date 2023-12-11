TITEL = "Programmiersprache B"

CONTENT = ("Entwicklung:\n"
	"-Ken Thompson und Dennis Ritchie entwickelten die Sprache „B“ (1969)\n"
	"-B ist stark beeinflusst von BCPL und dient als direkter Vorgänger der Programmiersprache C\n"
		"->BCPL ist der Vorgänger von B\n"
	"-wurde ursprünglich für die DEC PDP-7 mit 8 KB RAM entwickelt\n"
	"-später portiert auf PDP-11 Maschinen und Honeywell-Mainframes\n"
	"-wurde bis in die 1990er-Jahre verwendet\n"
		"-für beispielsweise AberMUD von Alan Cox\n"
"-konzipiert für ressourcenbeschränkte Systeme\n"
"-ermöglichte die Entwicklung des Unix-Betriebssystems\n"
"-trug bei zur Schaffung portabler Software und hochrangiger Systemarchitekturen bei\n"
	"Eigenschaften:\n"
	"-fehlende BCPL-Merkmale aufgrund eingeschränkter Hardwareressourcen auf der PDP-7\n"
"-keine verschachtelten Funktionsdefinitionen möglich\n"
"-B-Compiler auf der PDP-7 erzeugte einfachen Zwischencode, der von einem Interpreter zur Laufzeit interpretiert werden musste\n"
"-es gab nur einen Datentyp, dessen Bedeutung sich erst durch die benutzten Operatoren und Funktionen ergab\n"
	"->B ist also eine typlose Sprache\n"
	"->benutzerdefinierte Datenstrukturen\n"
"-ist Maschinenunabhängig\n"
	"->erlaubt einmaliges Schreiben und Ausführung auf verschiedenen Systemen\n"
"-hat nur beschränkte Möglichkeiten für das Speichermanagement\n"
"-es fehlt die Unterstützung für moderne Konstrukte wie objektorientierte Programmierung\n"
"-enthält bereits viele Sprachmerkmale, die in C zu finden sind\n"
"-einige Programme sind auch heute noch problemlos mit aktuellen C-Compilern übersetzbar\n"
"-Ziel der Sprache sind die System-Programmierung und Betriebssystementwicklung\n"
"-Prinzipien und Eigenschaften beeinflussen weiterhin innovative Sprachen und Programmierpraktiken\n"
	"->wichtig für die technologische Entwicklung und Informatik\n"
"Codebeispiel:\n"
"main() {\n"
  "auto c;\n"
  "auto d;\n"
  "d=0;\n"
  "while(1) {\n"
    "c=getchar();\n"
    "d=d+c;\n"
    "putchar(c);\n"
  "}\n"
"}\n"
"-dieses Programm lässt sich auch heute noch mit C-Compilern übersetzen, ist jedoch kein ANSI C\n"
"Quellen:\n"
	"- https://de-academic.com/dic.nsf/dewiki/126054\n"
	"- https://www.devx.com/terms/b-programming-language/\n")

IMAGE_NAME = ""
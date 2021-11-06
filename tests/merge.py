from junitparser import JUnitXml as junit

xmlfull = junit.fromfile('test-results/junit.xml')
xmlja1 = junit.fromfile('test-results/junit1.xml')
xmlja2 = junit.fromfile('test-results/junit2.xml')
xmlja3 = junit.fromfile('test-results/junit3.xml')
xmlja4 = junit.fromfile('test-results/junit4.xml')
xmlja5 = junit.fromfile('test-results/junit5.xml')
xmlja6 = junit.fromfile('test-results/junit6.xml')
xmlja7 = junit.fromfile('test-results/junit7.xml')
xmlja8 = junit.fromfile('test-results/junit8.xml')

xmlen = junit.fromfile('test-results/juniten.xml')
xmlen1 = junit.fromfile('test-results/juniten1.xml')
xmlen2 = junit.fromfile('test-results/juniten2.xml')
xmlen3 = junit.fromfile('test-results/juniten3.xml')
xmlen4 = junit.fromfile('test-results/juniten4.xml')
xmlen5 = junit.fromfile('test-results/juniten5.xml')
xmlen6 = junit.fromfile('test-results/juniten6.xml')
xmlen7 = junit.fromfile('test-results/juniten7.xml')
xmlen8 = junit.fromfile('test-results/juniten8.xml')

xmlfull = xmlfull + xmlja1 + xmlja2 + xmlja3 + xmlja4 + xmlja5 + xmlja6 + xmlja7 + xmlja8 + xmlen + xmlen1 + xmlen2 + xmlen3 + xmlen4 + xmlen5 + xmlen6 + xmlen7 + xmlen8
xmlfull.write()

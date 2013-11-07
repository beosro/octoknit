namespace StitchPattern;

 use StitchPattern\Model\StitchPattern;
 use StitchPattern\Model\StitchPatternTable;
 use Zend\Db\ResultSet\ResultSet;
 use Zend\Db\TableGateway\TableGateway;

class Module
{
    public function getAutoloaderConfig()
    {
        return array(
            'Zend\Loader\ClassMapAutoloader' => array(
                __DIR__ . '/autoload_classmap.php',
            ),
            'Zend\Loader\StandardAutoloader' => array(
                'namespaces' => array(
                    __NAMESPACE__ => __DIR__ . '/src/' . __NAMESPACE__,
                ),
            ),
        );
    }

    public function getConfig()
    {
        return include __DIR__ . '/config/module.config.php';
    }

     public function getServiceConfig()
     {
         return array(
             'factories' => array(
                 'StitchPattern\Model\StitchPatternTable' =>  function($sm) {
                     $tableGateway = $sm->get('StitchPatternTableGateway');
                     $table = new StitchPatternTable($tableGateway);
                     return $table;
                 },
                 'StitchPatternTableGateway' => function ($sm) {
                     $dbAdapter = $sm->get('Zend\Db\Adapter\Adapter');
                     $resultSetPrototype = new ResultSet();
                     $resultSetPrototype->setArrayObjectPrototype(new StitchPattern());
                     return new TableGateway('album', $dbAdapter, null, $resultSetPrototype);
                 },
             ),
         );
     }
}
@Library('sfci-pipeline-sharedlib@master') _

def envDef = [buildImage: 'ops0-artifactrepo1-0-prd.data.sfdc.net/docker-sfci-dev/sfci/cache-as-a-service/caas-sfci-docker:96a50c1e138a10d7cf8e3acc5a7fcf68027e3f66', useOpenJDK: true]

executePipeline(envDef) 
{
 	stage('One'){
 		echo 'Entered in first stage'
 	}
 	stage('Two'){
 		echo 'Entered in second stage'
 	}
 	stage('Three'){
 		echo 'Entered in third stage'
 	}
 	
}
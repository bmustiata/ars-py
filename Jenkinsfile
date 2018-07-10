stage('Build executable') {
    node {
        deleteDir()
        checkout scm

        docker.build('arst')
              .inside {
            archiveArtifacts artifacts: '/src/dist/arst'
        }
    }
}

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('git_lib') {
                    git branch: "mod/104", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/git-lib.git"
                }
                dir ('git_lib/lib') {
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install gitdb2==2.0.4 --user
                pip2 install gitpython==2.1.8 --user
                /usr/bin/python ./test/unit/merge_repo/main.py
                /usr/bin/python ./test/unit/merge_repo/run_program.py
                /usr/bin/python ./test/unit/merge_repo/help_message.py
                /usr/bin/python ./test/unit/merge_repo/load_cfg.py
                /usr/bin/python ./test/unit/merge_repo/is_git_repo.py
                /usr/bin/python ./test/unit/merge_repo/prepare_mail.py
                /usr/bin/python ./test/unit/merge_repo/post_process.py
                /usr/bin/python ./test/unit/merge_repo/post_check.py
                /usr/bin/python ./test/unit/merge_repo/merge_project.py
                /usr/bin/python ./test/unit/merge_repo/send_mail.py
                /usr/bin/python ./test/unit/merge_repo/quarantine.py
                /usr/bin/python ./test/unit/merge_repo/quarantine_files.py
                /usr/bin/python ./test/unit/merge_repo/post_body.py
                /usr/bin/python ./test/unit/merge_repo/process_project.py
                /usr/bin/python ./test/unit/merge_repo/process_changes.py
                /usr/bin/python ./test/unit/merge_repo/merge.py
                /usr/bin/python ./test/unit/merge_repo/cleanup_repo.py
                /usr/bin/python ./test/unit/merge_repo/detach_head.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                sh 'rm -rf git_lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/merge-repo/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/merge-repo/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/merge-repo/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/merge-repo/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}

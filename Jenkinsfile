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
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                pip2 install mock --user
                pip2 install gitpython --user
                ./test/unit/git_class/gitmerge_init.py
                ./test/unit/git_class/gitmerge_create_gitrepo.py
                ./test/unit/git_class/gitmerge_set_remote.py
                ./test/unit/git_class/gitmerge_is_remote.py
                ./test/unit/git_class/gitmerge_process_dirty.py
                ./test/unit/git_class/gitmerge_process_untracked.py
                ./test/unit/git_class/gitmerge_is_dirty.py
                ./test/unit/git_class/gitmerge_is_untracked.py
                ./test/unit/git_class/gitmerge_git_fetch.py
                ./test/unit/git_class/gitmerge_rename_br.py
                ./test/unit/git_class/gitmerge_git_co.py
                ./test/unit/git_class/gitmerge_priority_merge.py
                ./test/unit/git_class/gitmerge_git_pu.py
                ./test/unit/git_class/gitmerge_commits_diff.py
                ./test/unit/git_class/gitmerge_is_commits_ahead.py
                ./test/unit/git_class/gitclass_init.py
                ./test/unit/git_class/gitclass_create_repo.py
                ./test/unit/git_class/gitclass_create_cmd.py
                ./test/unit/merge_repo/main.py
                ./test/unit/merge_repo/run_program.py
                ./test/unit/merge_repo/help_message.py
                ./test/unit/merge_repo/load_cfg.py
                ./test/unit/merge_repo/is_git_repo.py
                ./test/unit/merge_repo/prepare_mail.py
                ./test/unit/merge_repo/move.py
                ./test/unit/merge_repo/post_process.py
                ./test/unit/merge_repo/post_check.py
                ./test/unit/merge_repo/merge_project.py
                ./test/unit/merge_repo/send_mail.py
                ./test/unit/merge_repo/process_project.py
                ./test/unit/merge_repo/merge.py
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
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
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/merge-repo/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/merge-repo/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/merge-repo/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/merge-repo/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}


load init

@test "Check kubernetes cluster" {
    run kubectl get nodes
    [ $status = 0 ]
    [[ ${lines[0]} != "No resources found." ]]
}

@test "Check NodePort" {
    run kubectl get svc remodeling-service -o jsonpath='{.spec.ports[0].nodePort}'
    [ $status = 0 ]
    echo "Port is ${lines[0]}" >&3
    [[ "${lines[0]}" =~ ^3[0-9]{4}$ ]]
}

@test "Check Ngnix Service" {
    PORT=$(kubectl get svc remodeling-service -o jsonpath='{.spec.ports[0].nodePort}')
    echo "Try to Access $NODE:$PORT" >&3
    run curl -s $NODE:$PORT
    [ $status = 0 ]
    [[ "${lines[0]}" == *Hostname* ]]
}



cls
function register-movement($data)
{
    Invoke-RestMethod -Method Post -ContentType 'application/json' -Body $data -Uri 'http://127.0.0.1:5000/movement'
}

 $body = @{
    valor = 40000
    tipo_movimiento = "proveedor"
    codigo_asociado = "4555121"
    verificado = $true
}

register-movement (ConvertTo-Json $body)
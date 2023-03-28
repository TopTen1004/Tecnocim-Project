﻿using MediatR;
using Tecnocim.Alia.Application.Dtos;
using Tecnocim.Alia.Application.Responses;

namespace Tecnocim.Alia.Application.Queries;

public class GetRatiosCuentaResultadoByEmpresaIdQuery : IRequest<GenericResult<RatiosCuentaResultadoDto>>
{
    public GetRatiosCuentaResultadoByEmpresaIdQuery(int empresaId, object? usuario)
    {
        EmpresaId = empresaId;
        Usuario = usuario;
    }

    public int EmpresaId { get; }
    public object? Usuario { get; }
}

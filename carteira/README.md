<h3>PROJETO CONTROLE DE GASTOS PESSOAL. FEITO PARA ESTUDOS.</h3><br/>
<p>Projeto de controle de gastos para desktop feito em Python usando Tkinter. Sendo que o projeto ainda está sendo desenvolvido
e pode sofrer mudanças.</p>
<p>Ele conecta a um banco de dados Postgres. Os script para o SQL do bd São esses:</p>

<code>
CREATE TABLE public.pessoa
(
    id_pessoa integer NOT NULL DEFAULT nextval('pessoa_id_pessoa_seq'::regclass),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    usuario character varying(30) COLLATE pg_catalog."default" NOT NULL,
    pass character varying(40) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT pessoa_pkey PRIMARY KEY (id_pessoa)
);

CREATE TABLE public.conta
(
    id_conta integer NOT NULL DEFAULT nextval('conta_id_conta_seq'::regclass),
    saldo double precision NOT NULL DEFAULT 0,
    id_pessoa integer,
    CONSTRAINT conta_pkey PRIMARY KEY (id_conta),
    CONSTRAINT conta_id_pessoa_fkey FOREIGN KEY (id_pessoa)
        REFERENCES public.pessoa (id_pessoa) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE public.categoria
(
    id_categoria integer NOT NULL DEFAULT nextval('categoria_id_categoria_seq'::regclass),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    id_tipo integer,
    CONSTRAINT categoria_pkey PRIMARY KEY (id_categoria),
    CONSTRAINT tipofk FOREIGN KEY (id_tipo)
        REFERENCES public.tipo (id_tipo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE public.operacao
(
    id_operacao integer NOT NULL DEFAULT nextval('operacao_id_operacao_seq'::regclass),
    descricao character varying(100) COLLATE pg_catalog."default" NOT NULL,
    valor double precision NOT NULL,
    id_categoria integer NOT NULL,
    tipo character(1) COLLATE pg_catalog."default" NOT NULL,
    id_conta integer NOT NULL,
    data timestamp with time zone NOT NULL DEFAULT LOCALTIMESTAMP,
    CONSTRAINT operacao_pkey PRIMARY KEY (id_operacao),
    CONSTRAINT categoriafk FOREIGN KEY (id_categoria)
        REFERENCES public.categoria (id_categoria) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT operacao_id_conta_fkey FOREIGN KEY (id_conta)
        REFERENCES public.conta (id_conta) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE public.tipo
(
    id_tipo integer NOT NULL DEFAULT nextval('tipo_id_tipo_seq'::regclass),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tipo_pkey PRIMARY KEY (id_tipo)
);

CREATE OR REPLACE FUNCTION atualizasaldo() RETURNS trigger AS $$
DECLARE
	tipo char;
	valor float;
BEGIN
	if(TG_OP = 'DELETE') then
		tipo = OLD.tipo;
		valor = OLD.valor;
		if (tipo = 'E') then
			update conta 
			set saldo = saldo - valor
			WHERE id_conta = OLD.id_conta;

		elsif (tipo = 'S') then
			update conta 
			set saldo = saldo + valor
			WHERE id_conta = OLD.id_conta;

		end if;
		RETURN NULL;
	elsif(TG_OP = 'UPDATE') then
		tipo = NEW.tipo;
		valor = NEW.valor;
		if (tipo = 'E') then
			update conta 
			set saldo = saldo + valor
			WHERE id_conta = OLD.id_conta;

		elsif (tipo = 'S') then
			update conta 
			set saldo = saldo - valor
			WHERE id_conta = OLD.id_conta;

		end if;
		RETURN NULL;
	elsif(TG_OP = 'INSERT') then
		tipo = NEW.tipo;
		valor = NEW.valor;
		if (tipo = 'E') then
			update conta 
			set saldo = saldo + valor
			WHERE id_conta = NEW.id_conta;
		elsif (tipo = 'S') then
			update conta 
			set saldo = saldo - valor
			WHERE id_conta = NEW.id_conta;
		end if;
		RETURN NULL;
    end if;

END
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER tg_operacao 
AFTER INSERT OR UPDATE OR DELETE ON operacao 
FOR EACH ROW EXECUTE PROCEDURE atualizasaldo();

</code>


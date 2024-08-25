import axios from 'axios';



// Definimos la URL base de la API
// baseURL sera la ruta donde estaran todos los turnos
const baseURL = 'http://localhost:8080/api/turnos';

// Definimos la funcion que obtiene todos los turnos

export const getTurnos = async () => {
	try {
		const response = await axios.get(baseURL);
		// response.data contiene la informacion que nos devuelve la API, ejemplo: { turnos: [] } o { turnos: [{...}, {...}] }
		return response.data;
	} catch (error) {
		console.error('Error en getTurnos:', error);
		return null;
	}
};

// Definimos la funcion que CREA un turno

export const createTurno = async (turno) => {
	try {
		const response = await axios.post(baseURL, turno);
		// response.data contiene la informacion que nos devuelve la API, ejemplo: { turno: {...} }
		return response.data;

	} catch (error) {

	console.error('Error en createTurno:', error);
		return null;

	}
}

// Definimos la funcion que ELIMINA un turno

export const deleteTurno = async (id) => {
	try {
		const response = await axios.delete(`${baseURL}/${id}`);
		// necesitamos retornar el turno actualizado al frontend para que se actualice en la vista y no se tenga que recargar la pagina xD

		return response.data;
	
	} catch (error) {
		console.error('Error en deleteTurno:', error);
		return null;
	}
}

// Definimos la funcion que ACTUALIZA un turno. supongo que esta es de las mas importantes poruqe aqui se utilizara el caso de uso de asignacion de mecanicos a los turnos correspondientes

le pasamos el id del turno y el turno actualizado
export const updateTurno = async (id, turno) => {
	try {
		const response = await axios.put(`${baseURL}/${id}`, turno);
		// necesitamos retornar el turno actualizado al frontend para que se actualice en la vista y no se tenga que recargar la pagina xD
		return response.data;
	} catch (error) {
		console.error('Error en updateTurno:', error);
		return null;
	}
}

// Definimos la funcion que OBTIENE un turno por su ID

export const getTurnoById = async (id) => {
	try {
		const response = await axios.get(`${baseURL}/${id}`);
		// response.data contiene la informacion que nos devuelve la API, ejemplo: { turno: {...} }
		return response.data;
	} catch (error) {
		console.error('Error en getTurnoById:', error);
		return null;
	}
}


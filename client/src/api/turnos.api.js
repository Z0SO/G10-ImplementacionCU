
import axios from 'axios';

// Definimos la URL base de la API
const baseURL = 'http://localhost:8080/api/turnos';

// Función para obtener el token de autenticación JWT desde el almacenamiento (localStorage, por ejemplo)
const getToken = () => {
    return localStorage.getItem('token'); // O desde sessionStorage, depende de tu implementación
};

// Función para configurar los encabezados de autorización
const getAuthHeaders = () => {
    const token = getToken();
    return {
        headers: {
            Authorization: `Bearer ${token}`
        }
    };
};

// Definimos la función que obtiene todos los turnos
export const getTurnos = async () => {
    try {
        const response = await axios.get(baseURL, getAuthHeaders());
        return response.data;
    } catch (error) {
        console.error('Error en getTurnos:', error);
        return null;
    }
};

// Definimos la función que CREA un turno
export const createTurno = async (turno) => {
    try {
        const response = await axios.post(baseURL, turno, getAuthHeaders());
        return response.data;
    } catch (error) {
        console.error('Error en createTurno:', error);
        return null;
    }
};

// Definimos la función que ELIMINA un turno
export const deleteTurno = async (id) => {
    try {
        const response = await axios.delete(`${baseURL}/${id}`, getAuthHeaders());
        return response.data;
    } catch (error) {
        console.error('Error en deleteTurno:', error);
        return null;
    }
};

// Definimos la función que ACTUALIZA un turno
export const updateTurno = async (id, turno) => {
    try {
        const response = await axios.put(`${baseURL}/${id}`, turno, getAuthHeaders());
        return response.data;
    } catch (error) {
        console.error('Error en updateTurno:', error);
        return null;
    }
};

// Definimos la función que OBTIENE un turno por su ID
export const getTurnoById = async (id) => {
    try {
        const response = await axios.get(`${baseURL}/${id}`, getAuthHeaders());
        return response.data;
    } catch (error) {
        console.error('Error en getTurnoById:', error);
        return null;
    }
};

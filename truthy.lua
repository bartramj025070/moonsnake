--[[
	This should be ignored by Moonsnake.
	
	Moonsnake is an interpreter for Luau (@luau.org) built in Python,
	so that it can be used a module itself.
	
	It is deliberately written in python, for both readability and so
	that it can be used in stricter development environments that do
	not support running unknowns. This stops it being written in C++.
	
	Copyright 2026 kaleidoscopikatt
]]

local myModule = {}
myModule.__index = myModule

function myModule.new()
	local self = {
		
	}
	return setmetatable(self, myModule)
end

return myModule
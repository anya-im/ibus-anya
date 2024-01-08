# -*- coding: utf-8 -*-
# vim:set et sts=4 sw=4:
#
# ibus-anya - Anya engine for IBus
#
# Copyright (c) 2024 Masahiko Hashimoto <hashimom@geeko.jp>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import socket
import json


class AnyaAdaptor:
    def __init__(self, port=30055, timeout=10, buffer=1024):
        self._s_addr = ("0.0.0.0", port)
        self._timeout = timeout
        self._buffer = buffer
    
    def set_string(self, text):
        self.converted_text = self._convert(text)

    def get_nr_segments(self):
        return 1

    def get_segment(self, segment_index, candidate_index):
        return self.converted_text

    def get_nr_candidates(self, index):
        return 1

    def commit_segment(self, segment_index, candidate_index):
        pass

    def _convert(self, message: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(self._s_addr)

            msg = json.dumps({"op": "CONVERT", "args": {"pron": message}})
            s.send(msg.encode('utf-8'))

            rcv_msg = s.recv(self._buffer).decode('utf-8')
            rcv_msg = json.loads(rcv_msg)

        return rcv_msg["candidates"]["form"][0]

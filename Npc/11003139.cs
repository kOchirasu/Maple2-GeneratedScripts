using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003139: 
/// </summary>
public class _11003139 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0219154106000892$ 
                // - Hello, $MyPCName$!
                return default;
            case 30:
                // $script:0219154106000895$ 
                // - Howdy, $MyPCName$! I'm $npcName:11001003[gender:0]$. Do you want to learn more about the events we're running today? 
                switch (selection) {
                    // $script:0219154106000896$
                    // - Who's the woman standing next to you?
                    case 0:
                        return (35, NpcTalkButton.Close);
                }
                return default;
            case 35:
                // $script:0219154106000897$ 
                // - You mean $npcName:11001002[gender:1]$? That's my twin sister. She's also a dang good event guide, if you don't mind my saying. Whenever you're curious about any events in Maple World, we're the folks to talk to!
                return default;
        }
        
        return default;
    }
}

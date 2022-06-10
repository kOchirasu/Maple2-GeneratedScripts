using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003139: 
/// </summary>
public class _11003139 : NpcScript {
    internal _11003139(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0219154106000892$ 
                // - Hello, $MyPCName$!
                return true;
            case 30:
                // $script:0219154106000895$ 
                // - Howdy, $MyPCName$! I'm $npcName:11001003[gender:0]$. Do you want to learn more about the events we're running today? 
                switch (selection) {
                    // $script:0219154106000896$
                    // - Who's the woman standing next to you?
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0219154106000897$ 
                // - You mean $npcName:11001002[gender:1]$? That's my twin sister. She's also a dang good event guide, if you don't mind my saying. Whenever you're curious about any events in Maple World, we're the folks to talk to!
                return true;
            default:
                return true;
        }
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001003: Bobby
/// </summary>
public class _11001003 : NpcScript {
    internal _11001003(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0406144907006012$ 
                // - Hello, $MyPCName$!
                return true;
            case 40:
                // $script:0913145407011305$ 
                // - Howdy, $MyPCName$! I'm $npcName:11001003[gender:0]$. Do you want to learn more about the events we're running today? 
                switch (selection) {
                    // $script:0913145407011306$
                    // - Who's the girl in the matching outfit?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0913145407011307$ 
                // - You mean $npcName:11001002[gender:1]$? That's my twin sister. She's also a dang good event guide, if you don't mind my saying. Whenever you're curious about any events in Maple World, we're the folks to talk to!
                return true;
            default:
                return true;
        }
    }
}

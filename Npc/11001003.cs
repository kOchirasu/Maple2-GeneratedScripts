using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001003: Bobby
/// </summary>
public class _11001003 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0406144907006012$
    // - Hello, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0913145407011305$
                // - Howdy, $MyPCName$! I'm $npcName:11001003[gender:0]$. Do you want to learn more about the events we're running today? 
                switch (selection) {
                    // $script:0913145407011306$
                    // - Who's the girl in the matching outfit?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0913145407011307$
                // - You mean $npcName:11001002[gender:1]$? That's my twin sister. She's also a dang good event guide, if you don't mind my saying. Whenever you're curious about any events in Maple World, we're the folks to talk to!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

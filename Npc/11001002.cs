using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001002: Ruby
/// </summary>
public class _11001002 : NpcScript {
    protected override int First() {
        return 90;
    }

    // Select 0:
    // $script:0406144907006007$
    // - Good to see you, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (90, 0):
                // $script:0913145407011302$
                // - Hello, $MyPCName$! I'm $npcName:11001002[gender:1]$, and I'm here to talk to you about events. What would you like to know? 
                switch (selection) {
                    // $script:0913145407011303$
                    // - Who's the guy in the matching outfit?
                    case 0:
                        return 91;
                }
                return -1;
            case (91, 0):
                // $script:0913145407011304$
                // - That's my twin brother and fellow event guide. Come find us anytime you want to know about current events in Maple World. That's why we're here!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (90, 0) => NpcTalkButton.SelectableDistractor,
            (91, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

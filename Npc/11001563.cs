using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001563: Ishura
/// </summary>
public class _11001563 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006051$
    // - You're here.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006106$
                // - $MyPCName$, $npcName:11001232[gender:1]$ says she misses you. 
                return 10;
            case (10, 1):
                // $script:0515180307006107$
                // - I'm sorry I didn't stay in touch. I couldn't find the time. Still, it seems you did well enough without me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

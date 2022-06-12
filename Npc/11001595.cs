using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001595: Asimov
/// </summary>
public class _11001595 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006083$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006132$
                // - $npcName:11001229[gender:0]$'s body may be asleep, but I don't think his mind is. He'll return to us soon. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

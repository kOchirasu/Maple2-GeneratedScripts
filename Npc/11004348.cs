using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004348: Claus
/// </summary>
public class _11004348 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011755$
    // - I hope this hasn't been too hard on poor $npcName:11004345[gender:1]$...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011756$
                // - Is my family safe? What a stressful season this has been.
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

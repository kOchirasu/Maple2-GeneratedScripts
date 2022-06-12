using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003515: Chipo
/// </summary>
public class _11003515 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0817044507008831$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0817044507008834$
                // - Can I help you?
                switch (selection) {
                    // $script:0817044507008835$
                    // - Tell me about the five auras.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0817044507008836$
                // - The placas live in the desert to the southeast. If you defeat them while they're dancing, you can obtain their Essences of Dance.
                switch (selection) {
                    // $script:0817044507008837$
                    // - Tell me about placas.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0817044507008838$
                // - They look gentle, but I wouldn't touch them. Their thorns are sharp! 
                return 32;
            case (32, 1):
                // $script:0817044507008839$
                // - They're supposed to be good dancers, but I haven't seen it myself. They're not dancing all the time, you see. Do you think they prefer upbeat music?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003066: Dina
/// </summary>
public class _11003066 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0102155907007650$
    // - $MyPCName$, I'll always remember you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0102155907007651$
                // - I was told humans were selfish, foul creatures... but in the end, a human saved me.
                switch (selection) {
                    // $script:0102155907007652$
                    // - How do you feel?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0102155907007653$
                // - I'll live, thanks to you. We snowcubs are strong. That's all.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

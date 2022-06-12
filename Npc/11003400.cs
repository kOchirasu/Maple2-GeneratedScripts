using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003400: Rovey
/// </summary>
public class _11003400 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0621181107008568$
    // - Focus on your training.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0621181107008569$
                // - Willpower alone does not make you a knight.
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

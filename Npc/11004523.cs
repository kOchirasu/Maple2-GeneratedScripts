using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004523: Corny Soldieretto
/// </summary>
public class _11004523 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0103163407012500$
    // - Beeep... Beeep...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0103163407012501$
                // - Mathematical query: why was six afraid of seven?
                return 10;
            case (10, 1):
                // $script:0103163407012502$
                // - Answer: because seven ate nine. Ha! Ha! Ha! Ha!
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

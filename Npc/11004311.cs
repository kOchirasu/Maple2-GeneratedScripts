using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004311: Marianne
/// </summary>
public class _11004311 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0921211107011348$
    // - I hope I can see papa again soon...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0921211107011349$
                // - You're here! Just like you promised.
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

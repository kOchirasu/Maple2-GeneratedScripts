using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004115: Holstatt
/// </summary>
public class _11004115 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010473$
    // - I have no time for nonsense.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010474$
                // - Isn't there someone else you could be bothering?
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

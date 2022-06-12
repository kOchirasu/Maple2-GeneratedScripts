using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003402: Fredrik
/// </summary>
public class _11003402 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0621181107008571$
    // - This beats the slums, sure, but man...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0621181107008572$
                // - Listen, I don't really feel like talking.
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

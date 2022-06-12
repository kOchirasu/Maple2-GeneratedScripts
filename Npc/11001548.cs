using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001548: Suspicious Individual
/// </summary>
public class _11001548 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0629000607006395$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0629000607006396$
                // - I've got nothing to say to you.
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

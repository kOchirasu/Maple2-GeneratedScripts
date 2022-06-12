using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004403: Luanna
/// </summary>
public class _11004403 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011823$
    // - How can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011824$
                // - I pray this is a good omen.
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

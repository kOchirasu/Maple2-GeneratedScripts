using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001923: Fisher
/// </summary>
public class _11001923 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1121140707007424$
    // - I caught a prize fish!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1121184207007433$
                // - Hey! Find your own spot!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

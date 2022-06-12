using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003252: Merin
/// </summary>
public class _11003252 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0404104807008251$
    // - $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0404104807008252$
                // - I'm gonna be just as awesome as you when I grow up!
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

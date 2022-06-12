using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003879: Antonius
/// </summary>
public class _11003879 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0417135107009874$
    // - Hm. Those weeds are an eyesore...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009875$
                // - Hm. Those weeds are an eyesore...
                return -1;
            case (20, 0):
                // $script:0419172107009858$
                // - I think you forgot to take the lunch box. Here is an empty one.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

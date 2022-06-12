using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001538: Teresa
/// </summary>
public class _11001538 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0322222107005987$
    // - I didn't come all the way out here for nothing...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0329103507006004$
                // - I cannot help but sigh...
                //   <font color="#909090">She sighs.</font>
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

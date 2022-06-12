using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001912: Assistant Investigator
/// </summary>
public class _11001912 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1116181807007409$
    // - Hello. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1116181807007411$
                // - We need to track down Katvan's accomplices before they do any more damage.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000630: Kibu
/// </summary>
public class _11000630 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002533$
    // - Screeeeech!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002535$
                // - Have you heard how some people coddle their children? It's ridiculous to me! You've got to toughen up your kids, so they can fend for themselves in any situation!
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

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000392: Timus
/// </summary>
public class _11000392 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001592$
    // - Huh?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001594$
                // - Did you hear the court was canceled? I thought it would be a big to-do, so I arrived two weeks ago.
                return 20;
            case (20, 1):
                // $script:0831180407001595$
                // - And now it's canceled! Argh, I stayed at the hotel for two weeks for nothing!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

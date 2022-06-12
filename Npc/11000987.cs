using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000987: Horok
/// </summary>
public class _11000987 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003401$
    // - Hey, how did you find this place?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003403$
                // - It's coming, and we don't have much time left. We must find shelter quickly. 
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

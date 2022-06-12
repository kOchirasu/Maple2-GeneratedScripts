using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000189: Sylvia
/// </summary>
public class _11000189 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000830$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000833$
                // - I was sickly and weak as a child. Moving to $map:02000076$ improved my health tremendously.
                switch (selection) {
                    // $script:0831180407000834$
                    // - Where did you live before?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000835$
                // - Oh, near $map:02000100$. Have you been there? It's always kinda... overcast. Not sure why.
                return 31;
            case (31, 1):
                // $script:0831180407000836$
                // - $MyPCName$, if you haven't bought a house, you should consider one in $map:02000076$.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

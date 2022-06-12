using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003784: Veliche
/// </summary>
public class _11003784 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30
    }

    // Select 0:
    // $script:1213192607009638$
    // - Need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1213192607009639$
                // - The future is in our hands.
                return -1;
            case (20, 0):
                // $script:0131125107009814$
                // - Need something?
                return 20;
            case (20, 1):
                // $script:0131125107009815$
                // - It seems you came up to keep us supplied.
                //   There's no time to waste. Head to <font color="#ffd200">$map:52010063$</font> right away.
                return 20;
            case (20, 2):
                // functionID=1 
                // $script:0131125107009817$
                // - I'll arrange a transport for you.
                return -1;
            case (30, 0):
                // $script:0131125107009816$
                // - The future is in our hands.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

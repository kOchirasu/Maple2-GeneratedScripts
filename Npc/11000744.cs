using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000744: Sikken
/// </summary>
public class _11000744 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002888$
    // - I may be old, but I'm young at heart. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002890$
                // - Don't judge a book by its cover. I may be old, but I'm still a girl on the inside.  
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

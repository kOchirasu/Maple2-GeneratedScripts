using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004329: Jorge
/// </summary>
public class _11004329 : NpcScript {
    internal _11004329(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011629$ 
                // - I see... What a novel approach.
                return true;
            case 20:
                // $script:1010140307011535$ 
                // - I see... What a novel approach.
                return true;
            case 10:
                // $script:1102172107011630$ 
                // - I see... What a novel approach.
                return true;
            case 30:
                // $script:1010140307011536$ 
                // - I see... What a novel approach.
                switch (selection) {
                    // $script:1010140307011537$
                    // - What are you working on there?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011538$ 
                // - Hm? Oh, I'm doing research on the magic of this continent!
                // $script:1010140307011539$ 
                // - The rumors have already spread as far as $map:02000023$ that the people of this continent practice a form of magic we've never seen.
                // $script:1010140307011540$ 
                // - There's no way that I would miss such a tantalizing opportunity for self-edification.
                // $script:1010140307011541$ 
                // - Just you wait! I'm on the verge of a groundbreaking discovery, one for the history books!
                switch (selection) {
                    // $script:0111232407012695$
                    // - I look forward to hearing all about it.
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:0111232407012696$ 
                // - Indeed!
                return true;
            default:
                return true;
        }
    }
}

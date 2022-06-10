using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000407: Hermit
/// </summary>
public class _11000407 : NpcScript {
    internal _11000407(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001651$ 
                // - What do you want to know?
                return true;
            case 10:
                // $script:0831180407001652$ 
                // - You're being very attentive. I'm glad I'm not boring you. Is there anything else you want to hear?
                switch (selection) {
                    // $script:0831180407001653$
                    // - Actually, I'd better be on my way.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180407001654$
                    // - Tell me another old story.
                    case 1:
                        Id = 21;
                        return false;
                    // $script:0831180407001655$
                    // - Tell me about what's going on now.
                    case 2:
                        Id = 22;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180407001656$ 
                // - I didn't know it was getting so late. The forest trail has been fraught with mushrooms and pigs. Please be safe.
                return true;
            case 21:
                // $script:0831180407001657$ 
                // - Another old story? What kind of story?
                switch (selection) {
                    // $script:0831180407001658$
                    // - Tell me about the sages and the Lapenta.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407001659$
                    // - Tell me about $npcName:11000075[gender:1]$ and the heroes.
                    case 1:
                        Id = 41;
                        return false;
                    // $script:0831180407001660$
                    // - Tell me about the Demon King and the power of darkness.
                    case 2:
                        Id = 51;
                        return false;
                    // $script:0831180407001661$
                    // - I'm not that interested in old stories, honestly.
                    case 3:
                        Id = 10;
                        return false;
                }
                return true;
            case 22:
                // $script:0831180407001700$ 
                // - About the present, eh? All right, what do you want to know?
                switch (selection) {
                    // $script:0831180407001701$
                    // - Tell me all about Maple World.
                    case 0:
                        Id = 61;
                        return false;
                    // $script:0831180407001702$
                    // - Tell me of the Shadow World.
                    case 1:
                        Id = 71;
                        return false;
                    // $script:0831180407001703$
                    // - I don't feel like stories about the present right now.
                    case 2:
                        Id = 10;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407001662$ 
                // - This world wouldn't have existed if it weren't for the sages and the Lapenta. Which story do you want to hear first?
                switch (selection) {
                    // $script:0831180407001663$
                    // - Let's hear about the sages.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0831180407001664$
                    // - I'm interested in the Lapenta.
                    case 1:
                        Id = 33;
                        return false;
                    // $script:0831180407001665$
                    // - How about a different old story?
                    case 2:
                        Id = 21;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407001666$ 
                // - Originally, each of the three sages was responsible for one aspect of the world. They governed life, space, and time to ensure the world remained in balance. Then one day... 
                // $script:0831180407001667$ 
                // - The Demon King emerged, intent on destroying the balance between the three fundamental powers. He wanted to overtake the world with his own dark powers, turning it to a realm of endless chaos and despair.
                // $script:0831180407001668$ 
                // - The Demon King was strong enough to match the combined powers of the sages. To defeat him, the sages were forced to sacrifice themselves to banish the Demon King. Their legacy lives on in the Lapentas which contain what's left of their powers. Now do you understand why the sages were so important?
                switch (selection) {
                    // $script:0831180407001669$
                    // - Yep!
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407001670$ 
                // - The Lapentas were created by the sages to protect this world from the Demon King. They gave their lives to grant us these powerful gifts.
                // $script:0831180407001671$ 
                // - The Green Lapenta  keeps the balance of life, the Blue Lapenta governs space, and the Red Lapenta maintains time.
                // $script:0831180407001672$ 
                // - These three Lapentas have formed a protective ward around this world, keeping the formidable Demon King and his dark power at bay. Hopefully that explains why the Lapentas are so important.
                switch (selection) {
                    // $script:0831180407001673$
                    // - Yep!
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001674$ 
                // - $npcName:11000075[gender:1]$ and the Four Heroes helped the sages protect this world against the Demon King. Whose story do you want to hear first?
                switch (selection) {
                    // $script:0831180407001675$
                    // - Let's start with $npcName:11000075[gender:1]$.
                    case 0:
                        Id = 42;
                        return false;
                    // $script:0831180407001676$
                    // - The Four Heroes sound important.
                    case 1:
                        Id = 43;
                        return false;
                    // $script:0831180407001677$
                    // - How about a different old story?
                    case 2:
                        Id = 21;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407001678$ 
                // - There has been an empress born to each generation of humans, destined to deliver the will of the divine as their messenger.
                // $script:0831180407001679$ 
                // - The empresses are selected by the will of the divine. The $npcName:11000075[gender:1]$ was chosen a long time ago and inherited the title from her predecessor.
                // $script:0831180407001680$ 
                // - After the three sages perished and left behind the Lapentas, the $npcName:11000075[gender:1]$ became the spiritual leader of Maple World. She was instrumental in rebuilding society after the Demon King nearly destroyed everything.
                // $script:0831180407001681$ 
                // - In the early stages of Maple World's reconstruction, the $npcName:11000075[gender:1]$ would hold open courts to allow the people to speak to her. In time, however, she ceased this practice. 
                // $script:0831180407001682$ 
                // - There has been much speculation over why she stopped holding court. Some said the $npcName:11000075[gender:1]$ was struck down by illness. Others said she was abducted by the reawakened Demon King. 
                // $script:0831180407001683$ 
                // - Whatever the case may be, the empress never lost the love and respect of her people. These rumors only show how concerned they are for her well-being. Do you understand the importance of $npcName:11000075[gender:1]$ now?
                switch (selection) {
                    // $script:0831180407001684$
                    // - Yep!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 43:
                // $script:0831180407001685$ 
                // - The Four Heroes are gone now, but their legend will live on. It is rare to find someone who does not know their names. 
                // $script:0831180407001686$ 
                // - There was the mysterious mage Lewit from Ellin Forest, hot-headed warrior Ten from the holy Vayar Mountains, righteous archer Haster from the Green Meadows, and carefree thief Catarva from Kerningdom.
                // $script:0831180407001687$ 
                // - The warrior Ten fell in battle against the Demon King himself. The other three heroes were asked by the $npcName:11000075[gender:1]$ to protect the Lapentas, rather than sacrifice themselves.
                // $script:0831180407001688$ 
                // - The mage Lewit was entrusted with the Green Lapenta of Life. He hid it in the depths of the Ellin Forest for safekeeping.
                // $script:0831180407001689$ 
                // - Archer Haster was entrusted with the Red Lapenta of Time. He hid it somewhere in the Green Meadows.
                // $script:0831180407001690$ 
                // - Thief Catarva was entrusted with the Blue Lapenta of Space. He hid it in a secret alcove within Kerningdom.
                // $script:0831180407001691$ 
                // - The three surviving heroes became the first guardians of the Lapentas and dedicated themselves to the task for the rest of their lives. And now you know the story of the Four Heroes, yes?
                switch (selection) {
                    // $script:0831180407001692$
                    // - Yep!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407001693$ 
                // - Not much is known about the Demon King. He was powerful enough to bring Maple World to its knees, and no one who challenged him lived to tell about it.
                // $script:0831180407001694$ 
                // - No one knows where he came from, how he came to be, or what made him so powerful.
                // $script:0831180407001695$ 
                // - What everyone DOES know is that the Demon King hails from a world of death, despair, and fear, permeated by the power of darkness that he wields so brutally.
                // $script:0831180407001696$ 
                // - People named this dark world the Shadow World, and despaired when they found that even the Lapentas themselves could not purge the darkness.
                // $script:0831180407001697$ 
                // - So long as the protective ward of the Lapentas lasts, Maple World will be safe. But there is always the fear that the Shadow World will find new ways into our world, and destroy it.
                // $script:0831180407001698$ 
                // - So, somewhere beyond the reaches of our peaceful, idyllic Maple World lies a realm of pure darkness and terror that seeks to destroy us all. Does that answer your question?
                switch (selection) {
                    // $script:0831180407001699$
                    // - Yep!
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 61:
                // $script:0831180407001704$ 
                // - Maple World is a collection of continents floating in a vast, endless ocean. The biggest continent of all is Victoria Island.
                // $script:0831180407001705$ 
                // - Victoria Island consists of the capital city of $map:02000001$, where $npcName:11000075[gender:1]$</font>'s palace stands, $map:02000076$, $map:02000023$, $map:02000051$, and $map:02000100$. Each of these areas has developed its own unique culture.
                // $script:0831180407001706$ 
                // - Among them, $map:02000001$ is a metropolis built around the $npcName:11000075[gender:1]$'s palace and protected by massive castle walls. It's the political, economic, and cultural center of Maple World.
                // $script:0831180407001707$ 
                // - $map:02000076$ was once a quiet hamlet on an empty prairie. Then a group of bow craftsmen joined it and made it thrive among hunters and adventurers. Its elder is called... $npcName:11000001[gender:0]$, I think. I've heard he's a respectable fellow.
                // $script:0831180407001708$ 
                // - $map:02000023$ started out as a village of fairies in the depths of the Ellin Forest. After ages of hiding from the greater world, they have consented to allowing humans to visit them.
                // $script:0831180407001709$ 
                // - $map:02000051$ is situated on the far side of the treacherous Vayar Mountains. Rugged descendants of powerful tribes live on those rocky cliffs, and only the hardiest travelers can make it up there to pay them a visit.
                // $script:0831180407001710$ 
                // - $map:02000100$ was created by the Kerning workers who stay cooped up inside their bunkers, inventing things and studying crafting skills. Even I haven't been down there yet, but I've heard their technology is astonishing.
                // $script:0831180407001711$ 
                // - In my time, a great many young people left their homes on Maple Island and traveled across the vast oceans, dreaming of adventures and new challenges that awaited them on Victoria Island. I don't know if that's still the popular thing to do... Come to think of it, I haven't left this cabin for a long time.
                // $script:0831180407001712$ 
                // - Perhaps, instead of listening to this old man prattle on, you should venture forth and learn about this world for yourself. But for now, is there another story you want to hear?
                switch (selection) {
                    // $script:0831180407001713$
                    // - Yep!
                    case 0:
                        Id = 22;
                        return false;
                }
                return true;
            case 71:
                // $script:0831180407001714$ 
                // - The Shadow World is a world of death, despair, and fear, created by the Demon King. The only thing keeping him and his darkness from spilling into Maple World is the Lapentas, the legacy of the sages.
                // $script:0831180407001715$ 
                // - After the sages perished, their Lapentas formed a protective ward around this world which keeps the Shadow World at bay.
                // $script:0831180407001716$ 
                // - However, some ten years ago, the Blue Lapenta of Space broke. That lifted the seal on the Land of Darkness, and allowed a gateway to the Shadow World to open.
                // $script:0831180407001717$ 
                // - It is believe that this tragedy occurred because a servant of the Demon King tricked a protector of the Lapenta.
                // $script:0831180407001718$ 
                // - Fortunately, we still have the other two Lapentas hidden away somewhere in Maple World. So long as they persist, the ward will keep us safe from evil.
                // $script:0831180407001719$ 
                // - The army is doing everything they can to prevent the darkness infecting the Land of Darkness and Shadow World from spreading, but...
                // $script:0831180407001720$ 
                // - Perhaps what the $npcName:11000075[gender:1]$ needs are great heroes who can preserve what peace we have.
                // $script:0831180407001721$ 
                // - I don't know if there are people strong enough to protect the $npcName:11000075[gender:1]$, the Lapentas, and this world against the Demon King and his darkness, though. Anyway, is there another story do you want to hear?
                switch (selection) {
                    // $script:0831180407001722$
                    // - Yep!
                    case 0:
                        Id = 22;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
